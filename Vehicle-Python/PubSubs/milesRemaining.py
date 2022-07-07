# from queue import Queue
from threading import Thread
import signal
import time
import queue
from queue import Queue

import sys

# IDL DATA IMPORTS
sys.path.insert(0, '../MessageFormats/Fuel/')
import Fuel as Fuel
sys.path.insert(1, '../MessageFormats/MpG/')
import MpG as MpG  

sys.path.insert(2, '../MessageFormats/MilesToRefuel/')
import MilesToRefuel as MilesToRefuel  

#ADT IMPORTS
sys.path.insert(3, '../ADTs/')
from Writers import *  
from Readers import *
from Calculators import *


def main():
    writers = []
    readers = []
    threads = []
    signal.signal(signal.SIGINT,
                  lambda sig, frame: (
                    print("\nStopped!"),
                    [reader.delete() for reader in readers],
                    sys.exit(0),
                  ))

    print("Press Ctrl+C to stop")

    readers.append(FuelGauge([Fuel, "Fuel", "FuelRemaining544645", FuelRL]))  # noqa: F405
    readers.append(MpGDisplay([MpG, "MpG", "MpGCumulative", MpGRL]))  # noqa: F405

    writers.append(MilesRemaining([MilesToRefuel, "MilesToRefuel", "MilesToRefuelTopic"]))

    # Add readers and start threads
    for reader in readers:
        threads.append(Thread(target=(reader.run), daemon=True))
        
    threadMpG = Thread(target=(writers[0].run), 
                        args=(
                            readers[0].dataQueue, 
                            readers[1].dataQueue,), 
                        daemon=True)

    for thread in threads:
        thread.start()
    threadMpG.start()

    signal.pause()


main()
