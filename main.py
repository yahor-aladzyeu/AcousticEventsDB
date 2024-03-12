import os
import numpy as np
import librosa
import soundfile as sf
import pyroomacoustics as pra
import matplotlib.pyplot as plt
from multiprocessing import Pool

# Define input and output paths
source_folder_path = 'D:\\Audio\\Input\\Nr.1'
output_base_path = 'D:\\Audio\\Output'

# Define room sizes for different room types
sizes = {
    'wardrobe': [1, 1, 2.5],
    'room': [6, 4, 2.5],
    'hall': [15, 30, 4],
    'corridor': [20, 2, 2.5],
    'cube': [5, 5, 5]

}

# Define acoustic materials and their properties
materials = {
    'concrete': {'absorption': 0.2, 'scattering': 0.1},
    'wood': {'absorption': 0.35, 'scattering': 0.2},
    'glass': {'absorption': 0.1, 'scattering': 0.05},
    'metal': {'absorption': 0.05, 'scattering': 0.03}

}

# Define Signal-to-Noise Ratios (SNRs) to be used
SNRs = [20, 50]

# Function to add white noise to a signal based on SNR
def add_white_noise(signal, snr_db):
    signal_power = np.mean(signal ** 2)
    noise_power = signal_power / (10 ** (snr_db / 10))
    white_noise = np.random.randn(len(signal)) * np.sqrt(noise_power)
    noisy_signal = signal + white_noise
    return noisy_signal

# Function to create a folder if it doesn't exist
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to plot grouped waveforms
def plot_grouped_waveforms(signals_dict, title, output_folder):
    plt.figure(figsize=(10, 4))
    for label, signal in signals_dict.items():
        plt.plot(signal[:1000], label=label)
    plt.title(title)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.tight_layout()
    plot_file_path = os.path.join(output_folder, f'graph.png')
    plt.savefig(plot_file_path)
    plt.close()

# Function to plot the spectrogram of a signal
def plot_spectrogram(signal, sr, output_file_path):
    plt.figure(figsize=(10, 4))
    D = librosa.amplitude_to_db(np.abs(librosa.stft(signal)), ref=np.max)
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.tight_layout()
    plt.savefig(output_file_path)
    plt.close()

# Function to plot common signals with SNR=50dB
def plot_common_snr_50dB(signals_dict, filename, room_type, output_base_path):
    common_output_folder = os.path.join(output_base_path, filename, room_type, 'Common_SNR50')
    create_folder_if_not_exists(common_output_folder)

    plt.figure(figsize=(10, 4))
    for material, signal in signals_dict.items():
        plt.plot(signal[:1000], label=material)
    plt.title(f'{filename} - {room_type} (SNR=50dB)')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.tight_layout()
    plot_file_path = os.path.join(common_output_folder, f'{room_type}_SNR50.png')
    plt.savefig(plot_file_path)
    plt.close()



def simulate_room(size_value, material_value, signal, sr, source_file_name, size_key, material_key, SNRs,
                  output_base_path):
    output_signals = {}
    # Create an output folder for the room simulation results
    room_output_folder = os.path.join(output_base_path, source_file_name, size_key, material_key)
    create_folder_if_not_exists(room_output_folder)

    # Create a ShoeBox room with specified size and materials
    room = pra.ShoeBox(
        size_value, fs=sr,
        materials=pra.Material(material_value['absorption'], material_value['scattering']),
        max_order=10
    )
    # Add a source and microphone to the room
    room.add_source([size_value[0] / 2, size_value[1] / 2, size_value[2] / 2], signal=signal)
    room.add_microphone([size_value[0] / 2, size_value[1] / 2, size_value[2] / 2 + 0.5])
    # Simulate the room acoustics
    room.simulate()

    # Store the clean signal
    output_signals['NoNoise'] = room.mic_array.signals[0, :]
    # Add white noise at different SNRs to the clean signal
    for snr in SNRs:
        noisy_signal = add_white_noise(output_signals['NoNoise'], snr)
        output_signals[f'SNR{snr}'] = noisy_signal

    # Save the simulated signals and their spectrograms
    for key, signal in output_signals.items():
        output_file_name = f'{source_file_name}_{size_key}_{material_key}_{key}'
        output_wav_path = os.path.join(room_output_folder, output_file_name + '.wav')
        output_spec_path = os.path.join(room_output_folder, output_file_name + '_spectrogram.png')

        # Save the signal as a WAV file
        sf.write(output_wav_path, signal, sr)
        # Plot and save the spectrogram
        plot_spectrogram(signal, sr, output_spec_path)


def process_file(filename):
    file_path = os.path.join(source_folder_path, filename)
    # Load the audio signal from the input file
    signal, sr = librosa.load(file_path, sr=None)
    source_file_name = os.path.splitext(filename)[0]

    # Simulate different room sizes and materials for the loaded signal
    for size_key, size_value in sizes.items():
        for material_key, material_value in materials.items():
            simulate_room(size_value, material_value, signal, sr, source_file_name, size_key, material_key, SNRs,
                          output_base_path)


if __name__ == "__main__":
    # Get a list of all WAV files in the source folder
    files = [f for f in os.listdir(source_folder_path) if f.lower().endswith('.wav')]
    # Use multiprocessing to process multiple files simultaneously
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(process_file, files)

    print("Generation process completed successfully!!!")
