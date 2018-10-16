"""Creates the virtual machine."""

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(unused_context):
  """Creates the first virtual machine."""

  resources = [{
      'name': 'gcp-first-template',
      'type': 'compute.v1.instance',
      'properties': {
          'zone': 'us-east1-b',
          'machineType': ''.join([COMPUTE_URL_BASE, 'projects/practicaldevopsgcp-197023',
                                  '/zones/us-east1-b/',
                                  'machineTypes/f1-micro']),
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                          'debian-cloud/global/',
                                          'images/family/debian-8'])
              }
          }],
          'networkInterfaces': [{
              'network': '$(ref.a-new-network.selfLink)',
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
          }]
      }
  }]
  return {'resources': resources}