import tensorflow as tf
import tensorflow_text as tf_text

directory_url = 'https://storage.googleapis.com/download.tensorflow.org/data/illiad/'
file_names = ['cowper.txt', 'derby.txt', 'butler.txt']

file_paths = [
    tf.keras.utils.get_file(file_name, directory_url + file_name)
    for file_name in file_names
]

dataset = tf.data.TextLineDataset(file_paths)

dataset = dataset.map(lambda txt : tf_text.normalize_utf8(txt)).shuffle(100).batch(32).repeat()