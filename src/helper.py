def check_config_file(data={}):
    
    config_keys = {"bsky_username", "fetch_period", "get_posts", "get_top_posts", "gen_avatar", "get_profile", "get_hashtags", "get_mentions"}

    return_string = ""

    for key in data.keys():
        if key in config_keys:
            config_keys.remove(key)
    
    if len(config_keys) != 0:
        for item in config_keys:
            return_string += f"{item}, "
        return_string = return_string[:-2]

    return (len(config_keys) == 0,return_string)
