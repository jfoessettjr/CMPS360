using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Module5.Pages;

public class AboutTheAppModel : PageModel
{
    private readonly ILogger<AboutTheAppModel> _logger;

    public AboutTheAppModel(ILogger<AboutTheAppModel> logger)
    {
        _logger = logger;
    }

    public void OnGet()
    {
        int number = 7;

            if (number > 0)
            {
                ViewData["Message"] = "This App is to show a basic design of what I can create in C# and dotnet core.";
            }
            else if (number < 0)
            {
                ViewData["Message"] = "This App is crap.";
            }
            else
            {
                ViewData["Message"] = "What is an App?";
            } 
        
    }
}