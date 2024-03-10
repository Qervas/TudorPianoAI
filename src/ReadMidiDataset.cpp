#include <iostream>
#include <filesystem>
#include "MidiFile.h"

using namespace smf;
namespace fs = std::filesystem;

void processMidiFile(const std::string& filePath) {
    MidiFile midiFile;
    midiFile.read(filePath);
    midiFile.doTimeAnalysis();  // Important: Analyze the file's timing
    midiFile.joinTracks();      // Merge all tracks for easier processing

    // Now, all events are in track 0
    int track = 0;

    std::cout << "Processing file: " << filePath << std::endl;

    for (int eventIndex = 0; eventIndex < midiFile[track].size(); eventIndex++) {
        MidiEvent& event = midiFile[track][eventIndex];

        if (!event.isNoteOn()) continue;

        int noteNumber = event.getKeyNumber();
        double startTime = event.seconds; // Start time in seconds

        // Search for corresponding note-off event to calculate duration
        double endTime = startTime; // Initialize with start time as fallback
        for (int offEventIndex = eventIndex + 1; offEventIndex < midiFile[track].size(); offEventIndex++) {
            MidiEvent& offEvent = midiFile[track][offEventIndex];
            if (offEvent.isNoteOff() && offEvent.getKeyNumber() == noteNumber) {
                endTime = offEvent.seconds;
                break; // Found the matching note-off event
            }
        }

        double duration = endTime - startTime;

        std::cout << "Note: " << noteNumber
                  << ", Start Time: " << startTime
                  << ", Duration: " << duration << " seconds" << std::endl;
    }
}

int main() {
    std::string directoryPath = "assets/midi";
    for (const auto& entry : fs::directory_iterator(directoryPath)) {
        if (entry.path().extension() == ".mid" || entry.path().extension() == ".midi") {
            processMidiFile(entry.path());
        }
    }

    return 0;
}
