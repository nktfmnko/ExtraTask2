from yandex_tracker_client import TrackerClient

file = open("id.txt")
token = file.readline().strip()
org_id = file.readline().strip()

client = TrackerClient(token=token, cloud_org_id=org_id)

issues = client.issues.get_all()
last_issue = str(issues[0])

try:
    client.issues.create(queue='TEAMCITYBUILDFA', summary=f"Issue № {last_issue[len(last_issue) - 2]}",
                         type={'name': 'Task'}, assignee='nktfmnko')
except Exception as ex:
    print("exception:\n", ex)
