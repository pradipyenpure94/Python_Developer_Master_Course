"""Guard clause example."""


def is_eligible_for_leave(employee) -> bool:
    return employee["is_active"] and employee["leave_balance"] > 0


def approve_leave(employee):
    if is_eligible_for_leave(employee):
        return "Leave request accepted"
    return "Leave request rejected"


def request_leave(employee):
    if is_eligible_for_leave(employee):
        return "Leave request submitted"
    return "Cannot submit leave request"
