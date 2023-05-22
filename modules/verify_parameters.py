from get_config_parameters import get_parameters

def parameters():
    class parameters():
        api_keys = get_parameters("ApiKeys")
        if len(str(api_keys)) < 14:
            print("Error: ApiKeys - must have a minimum of 14 digits")

        sound = get_parameters("sound")
        if sound != "off" and sound != "on":
            print("Error: sound - 'off' or 'on' is only what you can use")

        language = get_parameters("language")
        if language != "es" and language != "en":
            print("Error: language - 'es' or 'en' is only what you can use")

        media_type = get_parameters("media_type")
        if media_type != "video" and media_type != "photo":
            print("Error: media_type - 'video' or 'photo' is only what you can use")

        orientation = get_parameters("orientation")
        if orientation != "landscape" and orientation != "portrait" and orientation != "square":
            print("Error: orientation - 'landscape', 'portrait' or 'square' is only what you can use")

        size = get_parameters("size")
        if size != "large" and size != "medium" and size != "small" and size != "original" and size != "large2x" and size != "large":
            print("Error: size - 'large', 'medium' or 'small' or 'original' or 'large2x' or 'large'  is only what you can use")

        page = get_parameters("page")
        if type(page) != int:
            page = 1
            print("Warning: page - default is always set to 1")

        per_page = get_parameters("per_page")
        if type(per_page) != int:
            per_page = 2
            print("Warning: per_page - default is always set to 2")

        query = get_parameters("query")

        save = get_parameters("save")
        if save.endswith("/"):
            save = save[:-1]
            print("Error: save - must be a directory path")

        resolution = get_parameters("resolution")
        if resolution != "16:9" and resolution != "9:16":
            print("Error: resolution - '16:9' or '9:16' is only what you can use")

        typedownload = get_parameters("typedownload")
        if typedownload != "query":
            print("Error: typedownload - 'query' is only what you can use")
        
        media_type = get_parameters("media_type")

    return parameters()

params = parameters()
