using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Module5.Pages;

public class EmploymentModel : PageModel
{
    private readonly ILogger<EmploymentModel> _logger;

    public EmploymentModel(ILogger<EmploymentModel> logger)
    {
        _logger = logger;
    }

    public void OnGet()
    {
    }
}