def GenerateConfig(context):
  """Creates the virtual machine with environment variables."""

  resources = [{
      'name': 'gcp-template-environment',
      'type': 'compute.v1.instance',
      'properties': {
          'zone': context.properties['zone'],
          'machineType': ''.join(['https://www.googleapis.com/compute/v1/',
                                  'projects/my-project/zones/',
                                  context.properties['zone'], '/machineTypes/',
                                  context.properties['machineType']]),
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage': ''.join(['https://www.googleapis.com/compute/v1/', 'projects/',
                                          'debian-cloud/global/',
                                          'images/family/debian-8'])
              }
          }],
          'networkInterfaces': [{
              'network': '$(ref.' + context.properties['network']
                         + '.selfLink)',
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
          }]
      }
  }]
  return {'resources': resources}
