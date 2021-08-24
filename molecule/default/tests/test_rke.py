import testinfra.utils.ansible_runner
import os


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


#Verificando binarios, arquivos e versões

def test_hosts_file(host):

    for name in (
     "/usr/bin/kubectl",
     "/usr/bin/rke",
     "/etc/docker/daemon.json",
     "/etc/sysctl.d/k8s.conf",
    ):

        f = host.file(name).exists

def test_docker_kubectl_is_installed(host):
    
    version = ['5:20.10','5:20.10','1.4.9','1.22']
    packages = ['docker-ce','docker-ce-cli','containerd.io','kubectl']

    for i, name in enumerate(packages):

        docker = host.package(name)
        assert docker.is_installed
        assert docker.version.startswith(version[i])

# Verificando se docker está rodando


def test_if_container_is_executing(host):
    cmd = host.run("docker container run -d --name molecule_nginx nginx")

    assert cmd.rc == 0

def test_if_container_is_runing(host):
   container = host.docker("molecule_nginx")

   assert container.is_running


def test_if_container_is_removed(host):
    cmd = host.run("docker container rm -f molecule_nginx")

    assert cmd.rc == 0


# Verificando conteudo de arquivos

def test_if_ssh_config_is_ok(host):

    conteudo = ['AllowTcpForwarding yes','net.bridge.bridge-nf-call-iptables']
    path = ['/etc/ssh/ssh_config','/etc/sysctl.d/k8s.conf']
    for i, name in enumerate(path):

        file = host.file(name)
        assert file.contains(conteudo[i])

# Verificando usuário k8s

def test_if_user_k8s_exists(host):

    rke_user = host.user("k8s")

    assert rke_user.exists
    assert rke_user.groups == ['k8s', 'docker']