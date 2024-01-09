def property_serializer(property_entity)->dict:
    return{
        "IdProperty": str(property_entity["IdProperty"]),
        "Name": property_entity["Name"],
        "Address": property_entity["Address"],
        "Price": property_entity["Price"],
        "Year": property_entity["Year"],
        "CodeInternal": property_entity["CodeInternal"],
        "Owner": property_entity["Owner"].IdOwner,
    }

def list_property_serializer(property_entities)->list:
    return [property_serializer(property) for property in property_entities]

def property_image_serializer(property_image_entity)->dict:
    return{
        "IdPropertyImage":str(property_image_entity["IdPropertyImage"]),
        "IdProperty":property_image_entity["IdProperty"].IdProperty,
        "File":property_image_entity["File"],
        "Enabled":property_image_entity["Enabled"]
    }

def owner_serilizer(owner_entity)->dict:
    return{
        "IdOwner": owner_entity["IdOwner"],
        "Name": owner_entity["Name"],
        "Address": owner_entity["Address"],
        "Photo": owner_entity["Photo"],
        "Birthday": owner_entity["Birthday"]
    }