using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Module5.Pages;

public class PicturesModel : PageModel
{
    private readonly ILogger<PicturesModel> _logger;

    public PicturesModel(ILogger<PicturesModel> logger)
    {
        _logger = logger;
    }

    public void OnGet()
    {
    }
}