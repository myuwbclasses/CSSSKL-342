3.1.map_lookup -- map: [] adds missing keys, find doesn't

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra map_lookup.cpp -o map_lookup
    ./map_lookup

Output (g++ 11, cssimages/linuxlab):
    size 3, Mei 4307
    Ravi not found; size still 3
    ext["Ravi"] is 0
    size now 4
    Amir: 4102
    Mei: 4307
    Ravi: 0
    Zoe: 4410

valgrind: no errors, no leaks.

- ext["Zoe"] = 4410; adds Zoe, or overwrites Zoe's value if already there.
- ext.insert({"Mei", 4307}); adds only if the key is new: the second insert
  with 9999 changed nothing.
- ext.find("Ravi") just looks: it returns ext.end() when the key is missing,
  and the size stays 3.
- Just READING ext["Ravi"] ADDED Ravi, with the value 0 (an int's default):
  the size became 4. Use find to look without adding.
- Looping over a map visits the keys in sorted order (Amir, Mei, Ravi, Zoe),
  not in the order they were added. Each element is a pair:
  .first is the key, .second the value.
