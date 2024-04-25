"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""
import logging
from maya import cmds
import math

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

FOCAL_ATTR = "focalLength"


def calculate_distance(bounding_box_dimensions, cam):
    """ Given the bounding box dimensions and the camera fov, calculate the distance to move the camera.

    Args:
        bounding_box_dimensions: a dictionary containing width, height, depth.
        cam: the scene camera.
    Returns:
        distance: The distance to move the camera back.
    """

    horizontal_aperture = cmds.camera(cam, q=True, hfa=True)
    vertical_aperture = cmds.camera(cam, q=True, vfa=True)

    width = cmds.getAttr("defaultResolution.width")
    height = cmds.getAttr("defaultResolution.height")

    aspect_ratio = float(width) / float(height)

    bounding_box_dimensions['height'] = bounding_box_dimensions['height'] * aspect_ratio
    max_dimension = max(bounding_box_dimensions, key=bounding_box_dimensions.get)
    bounding_box_dimensions['height'] = bounding_box_dimensions['height'] / aspect_ratio

    log.debug('max_dimension: ' + max_dimension)

    object_size = bounding_box_dimensions[max_dimension]
    log.debug('object_size: ' + str(object_size))

    if max_dimension == 'width' or max_dimension == 'depth':
        fov = calculate_fov(cam, horizontal_aperture)
        padding = 1.2
    else:
        fov = calculate_fov(cam, vertical_aperture)
        padding = 1.2

    distance = abs(object_size / math.sin(fov)) * padding

    log.debug("Camera distance: {0}".format(distance))

    return distance

█
██████████████████████████████████
███████████████████████████████████████████████
█
██████████
████████████████████████████████████████████████████
        aperture: size of the camera aperture.
    Returns:
        The FOV in radians.
    """
    cam_shape = cmds.listRelatives(cam, shapes=True)[0]
    focal_attr = cam_shape + "." + FOCAL_ATTR
    focal = cmds.getAttr(focal_attr)
    print("focal length: " + str(focal))
    fov = 2.0 * math.atan(((aperture * 25.4) / (focal * 2.0)))

    log.debug("Camera Aperture: {0}".format(aperture))
    log.debug("Camera fov: {0}".format(fov))
    return fov


def get_width_height(bounding_box, rotation_axis):
    """ Get the width and height from the bounding box based on the rotation axis.

    Args:
        bounding_box: The bounding box min/max coordinates.
        rotation_axis: The axis used to rotate the camera for the turntable.
    Returns:
        width: The width of the bounding box.
        height: The height of the bounding box.
        depth: The depth of the bounding box.
        """
    width = None
    height = None
    depth = None
    if rotation_axis == "X" or rotation_axis == "Y":
        # Calculate width and height based off of X and Y coordinate values of the bounding box.  Calculated the same
        # if we're rotating on X or Y because both start facing in the Z axis at the object.
        width = abs(bounding_box[0]) + abs(bounding_box[3])
        height = abs(bounding_box[1]) + abs(bounding_box[4])
        depth = abs(bounding_box[2]) + abs(bounding_box[5])
█
█████████████████████████████
████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████
        depth = abs(bounding_box[1]) + abs(bounding_box[4])

    log.debug("Bounding box width: {0}".format(width))
    log.debug("Bounding box height: {0}".format(height))
    log.debug("Bounding box depth: {0}".format(depth))

    bounding_box_dimensions = {'width': width, 'height': height, 'depth': depth}

    return bounding_box_dimensions


def get_bounding_box(assets):
    """ Gets the bounding box of all meshes and standIns combined. """
    # First filter out other nodes except meshes.
    log.info("Calculating the bounding box...")
    mesh_nodes = []

    for asset in assets:
        asset_long = cmds.ls(asset, long=True)
        log.info("Getting mesh descendants for: {0}".format(asset))
        mesh_descendants = cmds.listRelatives(asset_long, allDescendents=True, fullPath=True, type="mesh",
                                              noIntermediate=True)
        log.info("Mesh descendants found: {0}".format(mesh_descendants))

        if mesh_descendants:
            for descendant in mesh_descendants:
                if cmds.nodeType(descendant) == "mesh" and descendant not in mesh_nodes:
                    mesh_nodes.append(descendant)

        if not mesh_descendants:
            log.info("Node has no descendants: {0}".format(asset))
███████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████
█
████████████████████████████████████████████████████
    asset_nodes = mesh_nodes
    if not asset_nodes or asset_nodes is None or not len(asset_nodes) > 0:
        raise ValueError("Unable to determine meshes")

    if not mesh_nodes:
        log.info("Skipping bounding box info for meshes as none were found.")
    else:
        log.info("Getting bounding box value from meshes: {0}".format(mesh_nodes))
        meshes_bb = cmds.exactWorldBoundingBox(mesh_nodes)
        log.info("Mesh bounding box values: {0}".format(meshes_bb))

    asset_bb = cmds.exactWorldBoundingBox(asset_nodes)
    log.info("Combined bounding box values (meshes & standIns): {0}".format(asset_bb))

    if all(bb == 0 for bb in asset_bb):  # Catch if ALL bounding box values are 0, as this should not happen.
        raise OSError("Unable to determine bounding box!")

    return asset_bb


def set_up_camera():
    # get assets
    assets = cmds.ls(visible=True, type="mesh", long=True)
    lightrig = cmds.ls('BTW_*:*', long=True, dag=1)
    assets = [item for item in assets if item not in lightrig]
    cmds.select(assets)

    # get parameters
    asset_bounding_box = get_bounding_box(assets)
    center_x = (asset_bounding_box[0] + asset_bounding_box[3]) / 2.0
    center_y = (asset_bounding_box[1] + asset_bounding_box[4]) / 2.0
    center_z = (asset_bounding_box[2] + asset_bounding_box[5]) / 2.0

████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████
███████████████████████████████████████████████
█
█████████████████████████████
    cmds.currentTime(1, edit=True)
    cmds.select('BTW_lightrig_components:render_cam')
    cmds.move(center_x, asset_bounding_box[1] + (height / 2.0),
              (max(bounding_box_dimensions['width'], bounding_box_dimensions['depth']) / 2.0) + distance + center_z)
    cmds.select('camera1_aim')
    cmds.move(center_x, center_y, center_z)
