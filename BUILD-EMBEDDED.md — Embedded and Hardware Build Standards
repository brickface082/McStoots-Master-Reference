# BUILD-EMBEDDED.md — Embedded and Hardware Build Standards
# McStoots Tech LLC | Load when building C, C++, Arduino, ESP-IDF projects

---

## SAFETY FIRST — READ BEFORE ANY HARDWARE TEST

1. Simulate first if at all possible
2. Define ALL failure modes before powering on
3. Document expected current draw, voltage, and timing
4. Test with safe input and limited power first
5. Never assume environment — verify with the actual device

---

## PROJECT STARTUP

```
project_root/
├── src/
│   ├── main/               # main application
│   │   └── main.c
│   ├── common/             # shared utilities
│   │   └── utils.c
│   └── drivers/            # hardware abstraction layer
├── include/                # all header files
│   ├── main/
│   └── common/
├── lib/                    # external libraries
├── tests/                  # unit tests
│   └── unit_tests/
├── docs/                   # schematics, pinouts, datasheets
├── config/
│   └── linker_scripts/
├── CMakeLists.txt          # or Makefile
└── README.md
```

---

## NAMING CONVENTIONS

| Thing | Convention | Example |
|-------|-----------|---------|
| Functions | snake_case | `read_sensor_value()` |
| Variables | snake_case | `sensor_reading` |
| Constants | UPPER_SNAKE_CASE | `MAX_BUFFER_SIZE` |
| Global constants | UPPER_SNAKE_CASE | `BAUD_RATE = 9600` |
| Structs, typedefs | PascalCase or _t suffix | `SensorData` or `sensor_data_t` |
| Pointer variables | p prefix | `pBuffer` |
| Private/internal | leading underscore | `_internal_calculate()` |
| Macros | UPPER_SNAKE_CASE | `#define LED_PIN 13` |

---

## NASA POWER OF 10 — MANDATORY FOR ALL EMBEDDED CODE

These rules apply to every file. No exceptions.

1. **Simple control flow** — no goto, no recursion, no deeply nested conditionals
2. **Bounded loops** — every loop has a hard maximum iteration count defined before the loop
3. **No dynamic memory in critical paths** — allocate at init, not during operation
4. **Functions fit on one screen** — if it scrolls, split it
5. **Two assertions per function minimum** — one on input, one on output
6. **Variables at smallest scope** — declare inside the block where used
7. **Check every return value** — if a function can fail, the caller checks
8. **Readable code** — no magic numbers, no clever tricks, no abbreviations
9. **One level of dereference** — no pointer-to-pointer-to-pointer chains
10. **Zero warnings** — compile with maximum warnings. All warnings are errors.

---

## EVERY C FUNCTION STRUCTURE

```c
/**
 * @brief Read temperature from sensor
 * @param sensor_pin GPIO pin number (0-39)
 * @param reading Output: temperature in Celsius
 * @return 0 on success, -1 on error
 */
int read_temperature(uint8_t sensor_pin, float* reading) {
    /* Input assertions — NASA Rule 5 */
    assert(sensor_pin <= 39);
    assert(reading != NULL);
    
    /* Implementation */
    float raw = analogRead(sensor_pin);
    *reading = (raw / 4095.0f) * 100.0f;
    
    /* Output assertion — NASA Rule 5 */
    assert(*reading >= -40.0f && *reading <= 125.0f);
    
    return 0;
}
```

---

## HEADER FILE STRUCTURE

```c
/* sensor.h */
#ifndef SENSOR_H        /* Include guard — required on every header */
#define SENSOR_H

#include <stdint.h>     /* Standard fixed-width types */
#include "config.h"     /* Project configuration */

/* Constants */
#define SENSOR_MAX_READING  4095
#define SENSOR_TIMEOUT_MS   1000

/* Type definitions */
typedef struct {
    float temperature;
    float humidity;
    uint32_t timestamp;
} SensorData_t;

/* Function declarations */
int sensor_init(uint8_t pin);
int sensor_read(SensorData_t* data);
void sensor_reset(void);

#endif /* SENSOR_H */
```

---

## MISRA C RULES (safety-critical builds)

Required for any code where failure causes physical risk:
- No dynamic memory allocation after init
- No goto
- No continue
- Array indexing only — no pointer arithmetic
- Explicit casting — no implicit type conversions
- No unreachable code

---

## ARDUINO-SPECIFIC

```cpp
void setup() {
    // Hardware init goes here — all of it, before loop()
    Serial.begin(9600);
    pinMode(LED_PIN, OUTPUT);
    sensor_init(SENSOR_PIN);
}

void loop() {
    // Keep loop() short
    // Move all logic to functions
    uint32_t iteration_count = 0;
    const uint32_t MAX_ITERATIONS = 1000;  // NASA Rule 2
    
    while (condition && iteration_count < MAX_ITERATIONS) {
        do_work();
        iteration_count++;
    }
}
```

---

## VERIFICATION CHECKLIST

- [ ] Compiles with zero warnings at maximum warning level
- [ ] Every loop has a hard iteration limit
- [ ] Every function has at minimum one input and one output assertion
- [ ] Every return value is checked
- [ ] No function is longer than one screen
- [ ] No dynamic memory allocation in the main execution path
- [ ] Tested with safe input and limited power before full operation
- [ ] Failure modes documented before power-on
