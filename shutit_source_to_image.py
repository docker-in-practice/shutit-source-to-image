"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class shutit_source_to_image(ShutItModule):


	def build(self, shutit):
		shutit.install('git')
		shutit.install('docker.io')
		shutit.install('wget')
		shutit.install('golang')
		shutit.send('wget -qO- https://download.docker.com/linux/static/stable/x86_64/docker-17.06.1-ce.tgz | tar -zxvf -')
		shutit.send('chmod +x docker/docker')
		shutit.send('mv docker/docker /usr/bin/docker')
		shutit.send('rm -rf docker')
		shutit.send('mkdir /root/go')
		shutit.send('export GOPATH=/root/go')
		shutit.add_to_bashrc('export GOPATH=/root/go')
		shutit.send('go get github.com/openshift/source-to-image')
		shutit.add_to_bashrc('export PATH=$PATH:${GOPATH}/src/github.com/openshift/source-to-image/_output/local/go/bin/')
		shutit.send('export PATH=$PATH:${GOPATH}/src/github.com/openshift/source-to-image/_output/local/go/bin/')
		shutit.send('cd ${GOPATH}/src/github.com/openshift/source-to-image')
		shutit.send('hack/build-go.sh')
		return True

	def get_config(self, shutit):
		# CONFIGURATION
		# shutit.get_config(module_id,option,default=None,boolean=False)
		#                                    - Get configuration value, boolean indicates whether the item is 
		#                                      a boolean type, eg get the config with:
		# shutit.get_config(self.module_id, 'myconfig', default='a value')
		#                                      and reference in your code with:
		# shutit.cfg[self.module_id]['myconfig']
		return True

	def test(self, shutit):
		# For test cycle part of the ShutIt build.
		return True

	def finalize(self, shutit):
		# Any cleanup required at the end.
		return True
	
	def is_installed(self, shutit):
		return False


def module():
	return shutit_source_to_image(
		'openshift.shutit_source_to_image.shutit_source_to_image.shutit_source_to_image', 1822046026.00,
		description='',
		maintainer='ian.miell@gmail.com',
		depends=['shutit.tk.setup']
	)

