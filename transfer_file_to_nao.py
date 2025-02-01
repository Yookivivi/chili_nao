import paramiko
from scp import SCPClient
from proxy import PEPPER_IP, username, password

def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def transfer_file_to_nao(local_path, nao_path, nao_ip, nao_username, nap_password):
    ssh = create_ssh_client(nao_ip, 22, nao_username, nap_password)

    # Create SCP client
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(local_path, nao_path)
        print("File {} has been transferred to {}".format(local_path, nao_path))

    # Close SSH connection
    ssh.close()

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

        # Use SCP to copy the file
        with ssh.open_sftp() as sftp:
            sftp.get(nao_path, local_path)
            print('Successfully copied {} to {}'.format(nao_path, local_path))

    except Exception as e:
        print('An error occurred: {}'.format(e))
    finally:
        ssh.close()

# remote_audio_path = "/home/nao/lbtaudio/playlist/eva_pre_mentor.wav"
# transfer_file_to_nao("audio_file/jerry_eva_pre_mentor.wav", remote_audio_path, PEPPER_IP, username, password)

# remote_audio_path = "/home/nao/lbtaudio/playlist/self_intro.wav"
# transfer_file_to_nao("audio_file/jerry_intro_nao.wav", remote_audio_path, PEPPER_IP, username, password)

# remote_audio_path = "/home/nao/lbtaudio/playlist/eva_after_mentor.wav"
# transfer_file_to_nao("audio_file/jerry_eva_after_mentor.wav", remote_audio_path, PEPPER_IP, username, password)

# remote_audio_path1 = "/home/nao/lbtaudio/playlist/lbt_pre_1.wav"
# transfer_file_to_nao("audio_file/lbt_pre_1.wav", remote_audio_path1, PEPPER_IP, username, password)

# remote_audio_path2 = "/home/nao/lbtaudio/playlist/lbt_pre_next_word.wav"
# transfer_file_to_nao("audio_file/lbt_pre_next_word.wav", remote_audio_path2, PEPPER_IP, username, password)