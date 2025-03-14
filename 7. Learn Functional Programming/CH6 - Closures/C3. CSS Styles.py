def css_styles(initial_styles):
    dict = initial_styles.copy()
    def add_style(selector, property, value):
        if selector not in dict:
            dict[selector] = {}
        dict[selector][property] = value
        return dict
        
    return add_style
