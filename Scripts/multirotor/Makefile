CXX        := 	clang++-5.0
CXXFLAGS   := 	-Wall -Wextra -stdlib=libc++ -std=c++14 -isystem
LDFLAGS    := 	-stdlib=libc++ -lc++ -lc++abi -lm -lc -lpthread \
				-lAirLib -lrpc -lMavLinkCom \
				-L$(SIMBOTIC_ROOT)/Plugins/AirSim/Source/AirLib/lib/x64/Debug
BUILD      := 	./build
OBJ_DIR    := 	$(BUILD)
TARGET     := 	multirotor
INCLUDE    := 	-I./ \
				-I$(SIMBOTIC_ROOT)/Plugins/AirSim/Source/AirLib/include \
				-I$(SIMBOTIC_ROOT)/Plugins/AirSim/Source/AirLib/deps/rpclib/include \
				-I$(SIMBOTIC_ROOT)/Plugins/AirSim/Source/AirLib/deps/eigen3 \
				-I/usr/include/libcxxabi \
				-I/usr/include

SRC        := $(wildcard *.cpp)
OBJECTS    := $(SRC:%.cpp=$(OBJ_DIR)/%.o)

all: build $(TARGET)

$(OBJ_DIR)/%.o: %.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) $(INCLUDE) -o $@ -c $<

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(INCLUDE) $(LDFLAGS) -o $(TARGET) $(OBJECTS)

.PHONY: all build clean debug release

build:
	@mkdir -p $(OBJ_DIR)
		
debug: CXXFLAGS += -DDEBUG -g
debug: all

release: CXXFLAGS += -O2
release: all

clean:
	-@rm -rvf $(OBJ_DIR)/*
	-@rm -rvf $(TARGET)
