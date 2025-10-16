---
date: '2021-06-20T00:00:00Z'
title: On Testing
tags:
- prose
- testing
---

## why?

- the only proper way to do any kind of research
- for quality assurance goals
- find and fix bugs as early as possible
- ensure code changes work as expected without breaking any released features


## Tests as in software system development

|name             |when to do            |done by whom                  |granularity         |whitebox/blackbox|tools                |business impact|
|-----------------|----------------------|------------------------------|--------------------|-----------------|---------------------|---------------|
|unit test        |during coding         |engineers                     |per function        |whitebox         |code libs            |none           |
|smoke test       |after coding          |engineers                     |per api, per service|blackbox         |cucumber, etc.       |none           |
|integration test |system integration    |engineers                     |per system          |blackbox         |cucumber, etc.       |none           |
|performance test |before release        |engineers                     |per system          |blackbox         |gatlin, jmeters, etc.|none           |
|regression test  |during & after release|engineers, product owners     |per system          |blackbox         |cucumber, etc.       |low            |
|alpha & beta test|after release         |product owners, selected users|per product         |blackbox         |                     |high           |




## Test case design criteria : what factors contribute to a "good" test case design (and how good is enough)?
- collectively exhaustive: cover all lines of codes / all possible use cases
- mutually exclusive: use as few test cases / codes  as possible
- rational methodology: 
  - repeatable: given inputs should have stable outputs
  - explicit inputs and outputs without side effects ( "pure" )
  - eliminate implicit variables, e.g. testing person biases, environment assumptions and dependencies
  - change only one variable per case

## Test framework criteria

- adaptive to code, input and environment changes
- open for extension, closed for modification
- fully integrated in all phases of development processes

## Tests are basically simulations

### Why test on simulations instead of "real" ones?
- test on real subjects are costly, in some cases with business impacts
- separation of testing subjects ( by defining a test scope ) to eliminate implicit variables and side effects

### Prerequisites for doing simulation tests
- subject codes rely on interfaces instead of specific implementations
- subject codes use dependency injection (all dependencies are specified in object creation)
- aspect oriented programming: subject codes have middleware injection points for testing purposes

### Variances of simulation objects
excerpt from http://xunitpatterns.com/Test%20Double%20Patterns.html

- spy: inputs and outputs recorder
- stub: spy + control inputs, respond with predefined outputs
- mock: stub + set expectations on calling behaviors
- fake: a simpler and "pure" implementation of an interface

## Mentality of testing

1. set up testing data and environments
2. define test cases that consist of :
  a. inputs that change only one variable at a time
  b. simulated inputs and outputs on dependencies
  3. expectations on outputs and dependency calling behaviors
3. run all cases, compare test results to expectations
4. build test reports, identify bugs and improvements in testing subjects and the testing itself.
5. repeat

## Process of writing unit tests for golang struct methods
- find the method's inputs (easy)
- find all callees (hard without tools, could use reflections )
- decide which callees should be mocked (easy if dependency is on interfaces)
- permute method inputs & mocked-callee input/outputs, in order to 
- cover all lines of code (whitebox testing)
- cover all possible use cases (blackbox testing)

## Golang unit test best practises

### test case structure
use subtests to run in parallel or case-by-case, with common steps defined in parent tests https://blog.golang.org/subtests

### test case naming
Test{function_name_of_test_subject}[_{sub_groups_of_cases}]

### error handling
for non-blocking issues, use testify.Assert or testing.Error
for blocing issues, use testing.Fatal

### test package naming

test code files are usually in the same package with subject code files.
could use "{pkg_name}_test" to break dependency loops in some cases.


## Reference links

http://xunitpatterns.com/Test%20Double%20Patterns.html
https://golang.org/doc/faq#Packages_Testing