from cta_bus_tracker import BusTracker


tracker = BusTracker()

# busses = tracker.get_vehicles(routes=[66])
# for bus in busses:
#     print(bus)

patterns = tracker.get_patterns(routes=["66"])
example_pattern = patterns[0]
for key, value in example_pattern.items():
    print(f"{key}\t\t{value}")