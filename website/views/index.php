<?php
const HOST = "theimperialgodwebsite.herokuapp.com";
const PORT = apache_getenv(".env.example");

class WebDashboard {
  public function __construct(User $user, int $ip) {
    const users = array(
      $user => $ip,
    )
    foreach($member of users) {
      if (users[$member] == $user) {return true;}
    }
    return false;
  }
  public function __destruct() {
    foreach($member of users) {
      if (users[$member] != $user && $user) {
        // lmao idk how to log them out...
      }
    }
  }
}
 ?>
