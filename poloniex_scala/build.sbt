name := "Project"

version := "1.0"

scalaVersion := "2.12.1"

libraryDependencies ++= Seq(
  "com.github.angiolep" % "akka-wamp_2.12" % "0.15.0"
)

libraryDependencies ++= Seq(
  "org.mongodb.scala" %% "mongo-scala-driver" % "2.0.0"
)
