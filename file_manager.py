import pickle

class FileManager:
    def load_data(self, name):
        with open(f'{name}.bin', 'rb') as f:
            data = pickle.load(f)
        return data
    
    def save_data(self, data):
        new_data = data
        level_int = new_data['level']
        with open(f'level_{level_int}.bin', 'wb') as f:
            pickle.dump(data, f)

test_data = {
    'level': 1,
    'obstacles': {
        'easy': 10,
        'medium': 5,
        'complex': 0,
    },
    'word': 'orange',
    'speed': 1,
}
f = FileManager()

f.save_data(test_data)

data = f.load_data('level_1')
print(data)