using Xunit;
using Moq;
using Microsoft.Extensions.Logging;
using KnowYourName.Api.Services;
using KnowYourName.Api.Models;

namespace KnowYourName.Tests.Services;

public class NameAnalysisServiceTests
{
    private readonly Mock<ILogger<NameAnalysisService>> _mockLogger;
    private readonly NameAnalysisService _service;

    public NameAnalysisServiceTests()
    {
        _mockLogger = new Mock<ILogger<NameAnalysisService>>();
        _service = new NameAnalysisService(_mockLogger.Object);
    }

    [Fact]
    public async Task AnalyzeNameAsync_WithValidName_ReturnsAnalysisResponse()
    {
        // Arrange
        var name = "John";

        // Act
        var result = await _service.AnalyzeNameAsync(name);

        // Assert
        Assert.NotNull(result);
        Assert.Equal(name, result.Name);
        Assert.NotNull(result.Origin);
        Assert.NotNull(result.Meaning);
        Assert.NotNull(result.Popularity);
        Assert.NotNull(result.FamousPeople);
        Assert.NotNull(result.CulturalSignificance);
    }

    [Theory]
    [InlineData("Mary")]
    [InlineData("David")]
    [InlineData("Sarah")]
    public async Task AnalyzeNameAsync_WithDifferentNames_ReturnsCorrectName(string inputName)
    {
        // Act
        var result = await _service.AnalyzeNameAsync(inputName);

        // Assert
        Assert.Equal(inputName, result.Name);
    }
}
