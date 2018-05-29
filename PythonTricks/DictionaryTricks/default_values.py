

name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    1241: 'Gilbert'
}


def greeting(userid):
    if userid in name_for_userid:
        return 'Hi %s!' % name_for_userid[userid]
    else:
        return 'Hi there!'


# Same
def greeting_2(user_id):
    try:
        return 'Hi {}!'.format(name_for_userid[user_id])
    except KeyError:
        return 'Hi there'


def greeting_3(user_id):
    return 'Hi {}!'.format(name_for_userid.get(user_id, 'there'))


print(greeting(382))
print(greeting(748219))

