"""
    With Yelp Wifi, users can go into their favorite local businesses and acces fast and free internet.
    These businesses can in turn keep in touch with their most loyal customerss by offering coupons and other updates through emails.
    If a user opts out of this service, we should take them off the mailing list.

    Given a list of users with opt-in statuses, and a sequential change log of opt-in status updates to be applied to the user list,
    return a list of user ids(sorted) that had their opt_in status changed after processing the logs

    Users not stored in our users list are considered opted-out.

    Example1 input:
    current_user_list = [
        User(1, false),
        User(19, true),
        User(4, true),
        User(54, false),
    ]
    opt_in_change_log = [
        OptInChange(19, 'opt_out'),
        OptInChange(19, 'opt_in'),
        OptInChange(1, 'opt_in'),
        OptInChange(71, 'opt_in'),
    ]
    Output: [1, 71]

    Example2 input:
    A = [
        User(1, false),
        User(19, true),
        User(4, true),
        User(54, false),
    ]
    B = [
        OptInChange(19, 'opt_out'),
        OptInChange(19, 'opt_in'),
        OptInChange(1, 'opt_in'),
        OptInChange(71, 'opt_in'),
        OptInChange(71, 'opt_out'),
    ]
    Output: [1]
"""


class User:
    def __init__(self, id, opted_in):
        self.id = id
        self.opted_in = opted_in


class OptInChange:
    def __init__(self, user_id, action):
        self.user_id = user_id
        self.action = action  # only 'opt_in' and 'opt_out'


def find_users_opted_in(current_user_list, opt_in_change_log):
    A = {}
    for obj in current_user_list:
        uid = obj.id
        b = obj.opted_in
        A[uid] = b
    B = {}
    for obj in opt_in_change_log:
        uid = obj.user_id
        b = True if obj.action == 'opt_in' else False
        B[uid] = b
    res = []
    for uid in B:
        if uid not in A and B[uid] == True:
            res.append(uid)
        elif uid in A and A[uid] != B[uid]:
            res.append(uid)
    return sorted(res)


# e.g.1
a = [
    User(1, False),
    User(19, True),
    User(4, True),
    User(54, False),
]
b = [
    OptInChange(19, 'opt_out'),
    OptInChange(19, 'opt_in'),
    OptInChange(1, 'opt_in'),
    OptInChange(71, 'opt_in'),
]
print(find_users_opted_in(a, b))

# e.g.2
a = [
    User(1, False),
    User(19, True),
    User(4, True),
    User(54, False),
]
b = [
    OptInChange(19, 'opt_out'),
    OptInChange(19, 'opt_in'),
    OptInChange(1, 'opt_in'),
    OptInChange(71, 'opt_in'),
    OptInChange(71, 'opt_out'),
]
print(find_users_opted_in(a, b))
