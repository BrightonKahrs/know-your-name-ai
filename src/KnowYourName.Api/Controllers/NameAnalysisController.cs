using Microsoft.AspNetCore.Mvc;
using KnowYourName.Api.Models;
using KnowYourName.Api.Services;

namespace KnowYourName.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class NameAnalysisController : ControllerBase
{
    private readonly INameAnalysisService _nameAnalysisService;
    private readonly ILogger<NameAnalysisController> _logger;

    public NameAnalysisController(INameAnalysisService nameAnalysisService, ILogger<NameAnalysisController> logger)
    {
        _nameAnalysisService = nameAnalysisService;
        _logger = logger;
    }

    [HttpPost("analyze")]
    public async Task<ActionResult<NameAnalysisResponse>> AnalyzeName([FromBody] NameAnalysisRequest request)
    {
        try
        {
            if (string.IsNullOrWhiteSpace(request.Name))
            {
                return BadRequest("Name is required.");
            }

            var result = await _nameAnalysisService.AnalyzeNameAsync(request.Name);
            return Ok(result);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error analyzing name: {Name}", request.Name);
            return StatusCode(500, "An error occurred while analyzing the name.");
        }
    }

    [HttpGet("health")]
    public IActionResult Health()
    {
        return Ok(new { Status = "Healthy", Timestamp = DateTime.UtcNow });
    }
}
