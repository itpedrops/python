import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
  if instance.tags:
    machine = None
    department = None
    project = None
    environment = None

    for tag in instance.tags:
      if tag['Key'] and tag['Key'] == 'DEPARTMENT':
        department = tag['Value']
      elif tag['Key'] and tag['Key'] == 'PROJECT':
        project = tag['Value']
      elif tag['Key'] and tag['Key'] == 'ENVIRONMENT':
        environment = tag['Value']

      if department is None and project is None and environment is None:
        machine =  'SEM TAG - ' + instance.instance_id
      else:
        machine = 'CORRETA - ' + instance.instance_id
      print machine
