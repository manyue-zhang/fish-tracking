import cv2
from background_subtraction.background_subtractor import BackgroundSubtractor
from Kalman_filter.object_tracking import tracking


if __name__ == "__main__":
    cap = cv2.VideoCapture("D:/Desktop/unterfish.mp4")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    background_subtractor = BackgroundSubtractor(width, height)
    print("Initialized background subtractor")

    tracking(cap, background_subtractor)

    # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()
