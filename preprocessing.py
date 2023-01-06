from sklearn.metrics import classification_report
from config.rating_args import *

def evaluation():
    ytrue = [1, 1, 0, 0]
    ypred = [1, 0, 0, 0]
    print(classification_report(ytrue, ypred, zero_division=0))




if __name__ == "__main__":
    # evaluation()

    rargs = RatingArgs()
    rargs.init_h_rating_args()

    # print(rargs.pp_threshold01)