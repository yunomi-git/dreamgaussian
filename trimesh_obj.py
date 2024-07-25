import trimesh
import trimesh_util
import numpy as np
from trimesh.visual.color import ColorVisuals
import trimesh.ray.ray_pyembree
import cv2

mesh_path = 'logs/Experiments/cartoon/bunny_pancake_image_sai_custom_1024/output_mesh.obj'
mesh = trimesh.load(mesh_path)
mesh_aux = trimesh_util.MeshAuxilliaryInfo(mesh)

visual = mesh.visual
num_vertices = len(mesh.vertices)

## SHOW
# trimesh_util.show_mesh(mesh)

def get_vertex_colors_from_uv(mesh: trimesh.Trimesh):
    num_vertices = len(mesh.vertices)
    vertex_colors = np.zeros((num_vertices, 4))
    image = mesh.visual.material.image

    for i in range(num_vertices):
        uv = mesh.visual.vertex_attributes.data['uv'][i]
        x = int(image.size[0] * uv[0])
        y = int(image.size[1] * (1.0 - uv[1]))
        # print(position)
        color = image.getpixel((x, y))
        vertex_colors[i, :3] = color
        vertex_colors[i, 3] = 255
    return vertex_colors

def grab_edge_magnitudes_from_uv(mesh: trimesh.Trimesh):
    img = np.array(mesh.visual.material.image)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 10)
    #
    # edges = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)  # Combined X and Y Sobel Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=10, threshold2=50)
    edges = edges.astype(float)
    # edges[edges < 0] = 0
    edges -= np.min(edges)
    edges /= np.max(edges)
    edges *= 255
    # edges[edges > 0] = 1.0
    # Blur again for smooth edges
    edges = cv2.GaussianBlur(edges, (5, 5), 20)
    edges = cv2.GaussianBlur(edges, (5, 5), 20)

    # cv2.imshow('Canny Edge', edges)
    # cv2.waitKey(0)

    vertex_colors = np.zeros(num_vertices)
    for i in range(num_vertices):
        uv = mesh.visual.vertex_attributes.data['uv'][i]
        x = int(img.shape[0] * uv[0])
        y = int(img.shape[1] * (1.0 - uv[1]))
        color = edges[y, x]
        vertex_colors[i] = color

    return vertex_colors

def convert_magnitudes_to_color_format(vertex_grayscale, include_alpha=False):
    if include_alpha:
        grayscale_colors = np.ones((len(vertex_grayscale), 4)) * 255
    else:
        grayscale_colors = np.ones((len(vertex_grayscale), 3)) * 255
    grayscale_colors[..., 0] = vertex_grayscale
    grayscale_colors[..., 1] = vertex_grayscale
    grayscale_colors[..., 2] = vertex_grayscale
    return grayscale_colors


def get_grayscale_magnitudes(vertex_colors, include_alpha=False):
    vertex_grayscale = np.dot(vertex_colors[..., :3], [0.2989, 0.5870, 0.1140])
    # grayscale_colors = convert_magnitudes_to_color_format(vertex_grayscale, include_alpha)
    return vertex_grayscale


vertex_colors = get_vertex_colors_from_uv(mesh)
edge_magnitudes = grab_edge_magnitudes_from_uv(mesh)
edge_colors = convert_magnitudes_to_color_format(edge_magnitudes, include_alpha=True)
grayscale_magnitudes = get_grayscale_magnitudes(vertex_colors, include_alpha=True)
vertex_grayscale_colors = convert_magnitudes_to_color_format(grayscale_magnitudes, include_alpha=True)

# Removes duplicate nodes while preserving colors
edge_weight = 1.0
color_combo = np.ones((num_vertices, 4)) * 255.0
color_combo[..., :3] = edge_weight * (255 - edge_colors[..., :3]) + (1.0 - edge_weight) * vertex_grayscale_colors[..., :3]


# make a new one
new_mesh = trimesh.load(mesh_path)
new_mesh.visual = ColorVisuals(mesh=new_mesh, face_colors=None, vertex_colors=color_combo)
new_mesh = new_mesh.process(merge_tex=True, merge_norm=True)

## Show
trimesh_util.show_mesh(new_mesh)


# Calculate deformations
# vertex_colors = mesh.visual.vertex_colors
# grayscale_magnitudes = get_grayscale_magnitudes(vertex_colors, include_alpha=True)
# vertex_grayscale = convert_magnitudes_to_color_format(grayscale_magnitudes, include_alpha=False) / 255

vertex_grayscale = new_mesh.visual.vertex_colors[..., :3] / 255.0
flip_magnitudes = True
if flip_magnitudes:
    vertex_grayscale = 1 - vertex_grayscale
vertex_grayscale -= np.min(vertex_grayscale)
vertex_grayscale /= np.max(vertex_grayscale)
vertex_normals = new_mesh.vertex_normals
scale = np.min(mesh_aux.bound_length) * 0.05

gray_avg = np.mean(vertex_grayscale)
# vertex_grayscale -= gray_avg
# vertex_grayscale[vertex_grayscale < 0] = 0
vertex_diff = (gray_avg - vertex_grayscale) * scale * vertex_normals
old_vertices = new_mesh.vertices.copy()
new_mesh.vertices += vertex_diff

trimesh.smoothing.filter_laplacian(new_mesh, lamb=0.1)

## SHOW
trimesh_util.show_mesh(new_mesh)

new_mesh.export("temp.obj")

s = trimesh.Scene()
vertices = new_mesh.vertices
vertex_grayscale_colors = get_grayscale_magnitudes(vertex_colors, include_alpha=True)
point_cloud = trimesh.points.PointCloud(vertices=mesh.vertices,
                                        colors=vertex_colors)
s.add_geometry(point_cloud)
s.add_geometry(new_mesh)
s.show()

print("")