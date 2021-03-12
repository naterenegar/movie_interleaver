
# Shot Boundary Detector. Init it, configure it, give it videos, and get a list
# of shots back
class SBD():

    def __init__():
        # TODO: Choice of algorithm?
        # TODO: Algo parameters?
        pass
   
    # Process buf of frames and return list of shots
    def process_frames(self, buf):
        pass

    #### Shuffle & Concatenate Functions ####

    # Takes buffer of frame and list of shots, then shuffles the list. Shuffles
    # the buf according to the shuffled list. Shuffles the list randomly
    def shuffle_shots_random(self, shots, buf):
        pass

    # Takes a list of buffers, each with a corresponding list of shots, and
    # interleaves the buffers
    # TODO: Add time tolerance and randomness parameters??
    def interleave_buffers(self, shotss, bufs):
        pass
