project(tqslib)

set(SRC
  bt/backtest.cpp
  bt/backtest.h
  rt/realtime.cpp
  rt/realtime.h
  bt/sim_context.cpp
  bt/sim_context.h
  bt/sim_data.cpp
  bt/sim_data.h
  bt/sim_trade.cpp
  bt/sim_trade.h
  stralet.cpp
  stralet.h
  tqs_cs.cpp
)

include_directories(
  .
  bt
  rt
  ../api
)

add_library(tqs-static STATIC ${SRC})
target_link_libraries(tqs-static jsoncpp)

add_library(tqs SHARED ${SRC})

target_link_libraries(tqs jsoncpp myutils tqapi)

add_executable(tqs_demo 
  demo/demo.cpp
  demo/demo_rbreaker.cpp
  demo/demo_doublema.cpp
)

target_link_libraries(tqs_demo
  tqs-static
  tqapi-static
)

install(TARGETS tqs_demo RUNTIME DESTINATION bin)

install(TARGETS tqs DESTINATION bin)
