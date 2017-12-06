from keras.callbacks import Callback


class LearningRateManager():
    def __init__(self, learning_rate, decay=0.1, step_epochs=None):
        self.decay = decay
        self.learning_rate = learning_rate
        self.step_epochs = step_epochs

    def schedule(self, epoch):
        if epoch in self.step_epochs:
            self.learning_rate = self.learning_rate * self.decay
        return self.learning_rate


class MultiGPUModelCheckpoint(Callback):
    def __init__(self, save_path, cpu_model):
        self.save_path = save_path
        self.cpu_model = cpu_model

    def on_epoch_end(self, epoch, logs=None):
        val_loss = logs['val_loss']
        self.cpu_model.save(self.save_path.format(epoch, val_loss))
