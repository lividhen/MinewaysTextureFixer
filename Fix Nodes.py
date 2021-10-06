import bpy



# Run through all materials of the current blend file

for mat in bpy.data.materials:

    # If the material has a node tree

    if mat.node_tree:

        # Run through all nodes

        for node in mat.node_tree.nodes:

            # If the node type is texture

            if node.type == 'TEX_IMAGE':

                # Set the interpolation -> Linear, (default) Closest, Cubic, Smart
                node.interpolation = 'Closest'

                # Link alpha from image texture to alpha on principled bsdf
                mat.node_tree.links.new( mat.node_tree.nodes['Principled BSDF'].inputs['Alpha'], mat.node_tree.nodes['Image Texture'].outputs['Alpha'] )
                
                # Change Image Texture (Keep all quotes!)
                #bpy.data.images['Name_Of_Old_Texture.png'].filepath = 'C:\Path\To\New\Image.png'
                