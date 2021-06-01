
emotions_to_modes = {
                     "happy": {"ionian": ["C", "D", "E", "F", "G", "A", "B"],
                               "dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"],
                               "lydian": ["C", "D", "E", "F#", "G", "A", "B"],
                               "mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"]},
                     
                     "sad": {"aeolian": ["C", "D", "Eb", "F", "G", "Ab", "Bb"]},

                     "scared": {"locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]}, 

                     "angry": {"phrygian": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
                              "mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"]}, 

                     "neutral": {"dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"]}, 

                     "surprised": {"ionian": ["C", "D", "E", "F", "G", "A", "B"],
                                   "lydian": ["C", "D", "E", "F#", "G", "A", "B"]}, 

                     "disgusted": {"locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]}
                     }

modes_to_notes = {
                  "ionian": ["C", "D", "E", "F", "G", "A", "B"],
                  "aeolian": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],  
                  "dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"],
                  "phrygian": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
                  "lydian": ["C", "D", "E", "F#", "G", "A", "B"],
                  "mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"],
                  "locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"] 
                 }

modes_to_chords = {
                  "ionian": {"a": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"]},

                  "aeolian": {"a": ["Cm", "Fm", "Gm", "Cm"],
                              "b": ["Cm", "Bb", "Ab", "Gm", "Cm"],        
                              "c": ["Cm", "Bb", "Ab", "Bb", "Eb", "Gm", "Cm"],
                              "d": ["Cm", "Ab", "Eb", "Fm", "Cm"]},


                  "dorian": {"a": ["Cm", "F", "Cm", "Bb", "Cm", "Gm", "Cm"],
                             "b": ["Cm", "Bb", "F", "Gm", "Cm"],
                             "c": ["Cm", "Gm", "Cm", "F", "Bb", "Eb", "Bb", "Cm"]},

                  "phrygian": {"a": ["Cm", "Db", "Cm", "Ab", "Cm", "Eb", "Fm", "Cm"]},

                  "lydian": {"a": ["C", "D", "G", "C", "Am", "D", "G", "C"],
                             "b": ["C", "D", "Em", "Bm", "C", "D", "C"]},

                  "mixolydian": {"a": ["C", "F", "Gm", "C"],
                                 "b": ["C", "F", "Dm", "Gm", "Am", "Gm", "C"],
                                 "c": ["C", "Bb", "C", "F", "Gm", "Bb", "C"],
                                 "d": ["C", "Bb", "C", "F", "Gm", "Bb", "C"]},

                  "locrian": {"a": ["Bdim", "C", "Dm", "Em", "F", "G", "Am"]} 
                  
                  }
