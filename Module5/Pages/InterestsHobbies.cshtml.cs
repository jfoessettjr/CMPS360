using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Module5.Pages;

public class InterestsHobbiesModel : PageModel
{
    private readonly ILogger<InterestsHobbiesModel> _logger;

    public InterestsHobbiesModel(ILogger<InterestsHobbiesModel> logger)
    {
        _logger = logger;
    }

    public void OnGet()
    {
                 int number = 10;

            if (number > 0)
            {
                ViewData["Message"] = "I like computers.";
            }
            else if (number < 0)
            {
                ViewData["Message"] = "I don't like computers today.";
            }
            else
            {
                ViewData["Message"] = "What is a computer?";
            }   
    }
}