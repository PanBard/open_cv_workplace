from create_sample import Sample
from train_model_cascade import Training

def main():
    make_sample = Sample()
    make_sample.delete_old_sample()
    make_sample.run()

    do_training = Training()
    do_training.run()
main()