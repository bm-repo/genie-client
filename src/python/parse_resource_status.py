from shared.constants import ResourceStatus
def parse_resource_status(status, assignee):
    if status in ResourceStatus.terminal:  # resource in terminal state
        return ResourceStatus.Addressed
    elif ResourceStatus.no_action == status and assignee == ResourceStatus.engineer_not_assigned:
        return ResourceStatus.UnAssigned
    elif status in ResourceStatus.denied:
        return ResourceStatus.NotApplicable
    elif status == ResourceStatus.engineer_assigned or assignee is not None:
        return ResourceStatus.InProgressCollapse
