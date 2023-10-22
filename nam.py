
roles = {
    "ST": "Student",
    "REST": "Registered student",
    "AL": "Alumni",
    "AN": "Anonymous",
    "TE": "Teacher",
    "AD": "Admin"
}

users = [
    {
        "name": "Holly",
        "role": roles["ST"]
    },
    {
        "name": "Peter",
        "role": roles["ST"]
    },
    {
        "name": "Luke",
        "role": roles["ST"]
    },
    {
        "name": "Janis",
        "role": roles["TE"]
    },
    {
        "name": "Aretha",
        "role": roles["TE"]
    },
    {
        "name": "Ringo",
        "role": roles["AD"]
    }
]

modules = [
    {
        "title": "Computer basics",
        "teacher": "Janis",
        "registered": ["Peter"],
        "alumni": ["Luke", "Holly"]
    },
    {
        "title": "Python basics",
        "teacher": "Janis",
        "registered": ["Holly"],
        "alumni": [],
        "requirement": "Computer basics"
    },
    {
        "title": "Django basics",
        "teacher": "Aretha",
        "registered": [],
        "alumni": [],
        "requirement": "Python basics"
    }
]

module_permissions = {
    roles["AN"]: ["describe"],
    roles["ST"]: ["describe"],
    roles["REST"]: ["describe", "read", "comment"],
    roles["AL"]: ["describe", "read"],
    roles["TE"]: ["describe", "read"],
    roles["AD"]: ["describe", "read", "write", "comment"]
}


def is_student(p_user_name):
    
    for user in users:
        while p_user_name == user['name'] and user['role'] == roles['ST']:
            return module_permissions[user['role']]
    return 'no'

def is_teacher(p_user_name):
    for user in users:
        while p_user_name == user['name'] and user['role'] == roles["TE"]:
            return module_permissions[user['role']]
    return 'no'

def is_admin(p_user_name):
    for user in users:
        while p_user_name == user['name'] and user['role'] == roles["AD"]:
            return module_permissions[user['role']]
    return 'no'

def is_anonymous(p_user_name):
    for user in users:
        while p_user_name != user['name']:
            return module_permissions[roles["AN"]]
    return 'no'


def is_registered_student(p_user_name, p_module_name):
    for module in modules:
        while is_student(p_user_name) and p_user_name in module['registered'] and p_module_name == module['title']:
                return module_permissions[roles["REST"]]
    return 'no'       


def is_alumni(p_user_name, p_module_name):
    for module in modules:
        while is_student(p_user_name) and p_user_name in module['alumni'] and p_module_name == module['title']:
            return module_permissions[roles['AL']]
    return 'no'


def admin_in_teachers(p_user_name, p_module_name):

    for module in modules:
        while is_teacher(p_user_name) and p_module_name == module['title'] and p_user_name == module['teacher']:
            return module_permissions[roles['AD']]
    return 'no'


def has_permission(p_user_name, p_module_name, p_permission):
    while any(m_permission == p_permission for m_permission in is_admin(p_user_name)):
        return True
    while any(m_permission == p_permission for m_permission in admin_in_teachers(p_user_name, p_module_name)):
        return True
    while any(m_permission == p_permission for m_permission in is_registered_student(p_user_name, p_module_name)):
        return True
    while any(m_permission == p_permission for m_permission in is_teacher(p_user_name)):
        return True
    while any(m_permission == p_permission for m_permission in is_alumni(p_user_name, p_module_name)):
        return True
    while any(m_permission == p_permission for m_permission in is_student(p_user_name)):
        return True
    while any(m_permission == p_permission for m_permission in is_anonymous(p_user_name)):
        return True
    return False
        
        
for permission in module_permissions[roles["AD"]]:
    for module in modules:
        print(f"Can {permission.upper()} on {module['title'].upper()}?")
        print("Anonymous", has_permission("Somebody", module["title"], permission))
        for user in users:
            print(user["name"], has_permission(user["name"], module["title"], permission))