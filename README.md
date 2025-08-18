




One aspect to note about the examples is that there is no example with rules containing timestamps. This is because it is challenging to model these time requirements in a imperative engine. While possible, as can be seen from examples in other github, this requires introducing sync activities that store the timestamps, which effectively turns the time requirements into data requirements. On the other hand in the declarative approach we get timestamps from the log so we can explicitly model time requirements.
