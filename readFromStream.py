import cv2
import youtube_dl
import os

if __name__ == '__main__':

    video_url = 'https://www.youtube.com/watch?v=U_1dGWepwrk&feature=youtu.be'

    ydl_opts = {}

    # create youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    # set video url, extract video information
    info_dict = ydl.extract_info(video_url, download=False)

    # get video formats available
    formats = info_dict.get('formats', None)

    for f in formats:

        # I want the lowest resolution, so I set resolution as 144p
        if f.get('format_note', None) == '720p':

            # get the video url
            url = f.get('url', None)

            # open url with opencv
            cap = cv2.VideoCapture(url)
            # set number of frames
            cap.set(cv2.CAP_PROP_FPS, 5)

            # check if url was opened
            if not cap.isOpened():
                print('video not opened')
                exit(-1)

            try:
                # creating a folder named data
                if not os.path.exists('data'):
                    os.makedirs('data')

                # if not created then raise error
            except OSError:
                print('Error: Creating directory of data')

            currentframe = 0

            while True:
                # read frame
                ret, frame = cap.read()

                if ret:
                    # if video is still left continue creating images
                    name = './data/frame' + str(currentframe) + '.jpg'
                    print('Creating...' + name)

                    # writing the extracted images
                    cv2.imwrite(name, frame)

                    # increasing counter so that it will
                    # show how many frames are created
                    currentframe += 1
                else:
                    break

                # display frame
                cv2.imshow('frame', frame)

                if cv2.waitKey(30) & 0xFF == ord('q'):
                    break

            # release VideoCapture
            cap.release()

    cv2.destroyAllWindows()
