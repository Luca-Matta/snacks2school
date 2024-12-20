from snacks2school.models import Class

def create_classes():
    classes = [
        "1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H", "1I", "1L", "1M", "1N", "1O", "1P", "1Q", "1R", "1S",
        "2A", "2B", "2C", "2D", "2E", "2F", "2G", "2H", "2I", "2L", "2M", "2N", "2O", "2P", "2Q", "2R", "2S",
        "3A", "3B", "3C", "3D", "3E", "3F", "3G", "3H", "3I", "3L", "3M", "3N", "3O", "3P", "3Q", "3R", "3S",
        "4A", "4B", "4C", "4D", "4E", "4F", "4G", "4H", "4I", "4L", "4M", "4N", "4O", "4P", "4Q", "4R", "4S",
        "5A", "5B", "5C", "5D", "5E", "5F", "5G", "5H", "5I", "5L", "5M", "5N", "5O", "5P", "5Q", "5R", "5S"
    ]
    

    created_count = 0
    for class_name in classes:
        schoolClass, created = Class.objects.get_or_create(name=class_name)
        if created:
            created_count += 1
    
    print(f"Creati {created_count} oggetti classe nel database!")
