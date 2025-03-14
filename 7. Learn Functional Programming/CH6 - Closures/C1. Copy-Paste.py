def new_clipboard(initial_clipboard):
    dict = initial_clipboard.copy()
    def copy_to_clipboard(key, value):
        dict[key] = value
        return dict
    
    def paste_from_clipboard(key):
        if key not in dict:
            return ""
        else:
            return dict[key]
    
    return copy_to_clipboard, paste_from_clipboard
