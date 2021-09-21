courses = {
    "js": "JavaScript 101",
    "python": ["Python 101", "Python 201"],
    "html": "HTML 101"
}

# Older way of fetching info:
# print(courses)
# courses["js"]

# # Modern Ways:
# print(courses.get('js', None))     # available 
# print(courses.get('css', 'Default text in here'))  # unavailable
# print(courses.get('css', 'CSS 101'))    # default set of values


# Now a days:
if courses.get("css", None): # Default values or use None
    print("You are enrolled in CSS 101")