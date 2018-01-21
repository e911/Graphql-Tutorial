def update_create_instance(instance, args, exception=['id']):
    if instance:
        [setattr(instance, key, value) for key, value in args.items() if key not in exception]
        # you

    # caution if you literally cloned this project, then be sure to have
    # elasticsearch running as every saved instance must go through
    # elasticsearch according to the way this project is configured.
    instance.save()


    return instance