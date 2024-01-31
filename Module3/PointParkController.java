package com.example.springboot;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController

public class PointParkController {

    @RequestMapping("/burgh")
    public String burgh(){
        boolean isHockeySeason = true;

        if (isHockeySeason) {
            return "Welcome to Penguin Country! It is Hockey season!";
        } else {
            return "Welcome to Penguin Country! but it is not Hockey season.";
        }
    }
    
    @RequestMapping("/about")
    public String about(){
        int currentYear = 2024;

        if (currentYear > 2020) {
            return "This is the story of a dude name Joel. It is the future!";
        } else {
            return "This is the story of a dude name Joel. It is the past Whoa!";
        }
    }


    @RequestMapping("/home")
    public String home(){
        boolean isErie = true;

        if (isErie) {
        return "The Gem City...The 'mistake' by the lake";
    } else {
        return "Not the correct city hehe!";
    }
}

    @RequestMapping("/interest")
    public String interest(){
        int favoriteNumber = 87;

        if (favoriteNumber == 87) {
            return "Beer, Music, Computers - some of my favorite things";
        } else {
            return "If you don't know my favorite number you can't know my favorite things";
        }
    }
}
