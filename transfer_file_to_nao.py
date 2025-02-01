import paramiko
from scp import SCPClient
from proxy import PEPPER_IP, username, password, audio_player

def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

# Function to transfer a file from the local machine to the NAO robot
def transfer_file_to_nao(local_path, nao_path, nao_ip, nao_username, nap_password):
    ssh = create_ssh_client(nao_ip, 22, nao_username, nap_password)
    # Create SCP client
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(local_path, nao_path)
        print("File {} has been transferred to {}".format(local_path, nao_path))
    # Close SSH connection
    ssh.close()

# Function to transfer a file from the NAO robot to the local machine
def transfer_file_from_nao(nao_path, local_path, nao_ip, nao_username, nao_password):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        # Load system host keys
        ssh.load_system_host_keys()
        # Set policy to add the server's host key automatically
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the NAO robot
        ssh.connect(nao_ip, username=nao_username, password=nao_password)

        # Use SFTP to copy the file
        with ssh.open_sftp() as sftp:
            sftp.get(nao_path, local_path)
            print('Successfully copied {} to {}'.format(nao_path, local_path))

    except Exception as e:
        print('An error occurred: {}'.format(e))
    finally:
        ssh.close()

# Example usage
remote_audio_path = "/home/nao/audio/wav/lbt_pre_1.wav"
transfer_file_to_nao("lbt_pre_1.wav", remote_audio_path, PEPPER_IP, username, password)
audio_player.playFile(remote_audio_path)
