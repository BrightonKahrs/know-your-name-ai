FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 8080
EXPOSE 8081

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["src/KnowYourName.Api/KnowYourName.Api.csproj", "src/KnowYourName.Api/"]
RUN dotnet restore "src/KnowYourName.Api/KnowYourName.Api.csproj"
COPY . .
WORKDIR "/src/src/KnowYourName.Api"
RUN dotnet build "KnowYourName.Api.csproj" -c $BUILD_CONFIGURATION -o /app/build

FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "KnowYourName.Api.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "KnowYourName.Api.dll"]
